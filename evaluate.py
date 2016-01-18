#coding=gbk
"""
Created on Sat Apr 18 09:36:37 2015

@author: zjh
"""
import cPickle,numpy,csv,sys

label_count={1:43,2:98,3:305,4:56,5:36,6:23,7:10,8:4,
             9:132,10:7,11:4,12:3,13:1,14:133,15:56,
             16:178,17:312,18:223,19:175}

def complete_evaluate(prediction,
                      answer,
                      csv_output='/home/liuxiaoming/bionlp_dl/result/result.csv'):
    def calculate(tp,pre_positive,class_num): 
        precision=tp/(pre_positive*1.+0.00000001)
        recall=tp/(label_count[class_num]*1.)
        f_score=2.0 * ((precision * recall)/(precision + recall+0.0000001))
        return precision,recall,f_score
    #答案列表
    def load_answer(answer):
        trigger_answer=open(answer)
        answer_list=[]
        for line in trigger_answer:
            label=line.split()[0]
            answer_list.append(int(float(label)))
        return answer_list
    #预测列表
    def load_prediction(prediction):
        trigger_pred=open(prediction)
        pred_list=[]
        for line in trigger_pred:
            label=line.split()[0]
            pred_list.append(int(float(label)))
        return pred_list
        
    csv_writer=csv.writer(open(csv_output,'wb'))
    csv_writer.writerow(['recall','precision','f_score'])
    list_answer=load_answer(answer)
    list_predict=load_prediction(prediction)
    assert len(list_answer)==len(list_predict)
    f_score_micro_avg_1=[]
    f_score_micro_avg_2=[]
    for num in xrange(19):
        num+=1
        tp=0
        pre_positive=0
        for index in xrange(len(list_answer)-1):
            p=int(list_predict[index])
            d=int(list_answer[index])
            if p==num:
                pre_positive+=1
            if p==d and p==num:
                tp+=1  
        print tp
        precision,recall,f_score=calculate(tp,pre_positive=pre_positive,class_num=num)
        csv_writer.writerow([precision,recall,f_score])        
        print '类别:%d,准确率:%f,召回率:%f,F值:%f'%(num,precision,recall,f_score)
        f_score_micro_avg_1.append(precision*recall)
        f_score_micro_avg_2.append(precision+recall)
    return 2*numpy.sum(f_score_micro_avg_1)/numpy.sum(f_score_micro_avg_2)

def simple_evaluate(prediction,test_set):
    def calculate(tp,fp,label_num):
        precision=tp/(tp+fp+0.000001)
        recall=tp/(label_num+0.0000001)
        f_score=2.0 * ((precision * recall)/(precision + recall+0.000001))
        return precision,recall,f_score
        
    def load_answer_from_file(test_set):
        trigger_answer=open(test_set)
        answer_list=[]
        for line in trigger_answer:
            line=line.split()
            answer_list.append(float(line[0]))
        return answer_list
        
    def load_answer(test_set):
        return test_set[1]
        
    def load_prediction(prediction):
        p=prediction
        return p.tolist()
             
    list_answer=load_answer(test_set)
        
    list_predict=load_prediction(prediction)
    f_score_micro_avg_1=[]
    f_score_micro_avg_2=[]
    all_tp=0.
    all_fp=0.
    for num in xrange(19):
        num+=1
        tp=0
        fp=0
        count=0
        for index in xrange(len(list_answer)-1):
            d=int(list_answer[index])
            if d==num:
                count+=1
        #if count<=5:
            #continue
        
        for index in xrange(len(list_answer)-1):
            p=int(list_predict[index])
            d=int(list_answer[index])
            if p==d and p==num:
                tp+=1
            if p==num and p!=d:
                fp+=1
        precision,recall,f_score=calculate(tp,fp,label_count[num])
        #print precision,recall,f_score
        f_score_micro_avg_1.append(precision*recall)
        f_score_micro_avg_2.append(precision+recall)
    
    for j in xrange(len(list_answer)-1):
        p=int(list_predict[j])
        d=int(list_answer[j])
        if(d==p and d!=0):
            all_tp+=1
        if d!=p and p!=0:
            all_fp+=1
    precision,recall,f_score=calculate(all_tp,all_fp,1809)
    #print len(f_score_mean)
    return precision,recall,f_score,2*numpy.sum(f_score_micro_avg_1)/(numpy.sum(f_score_micro_avg_2)+0.00001)

if __name__=='__main__':
    print sys.argv[0],sys.argv[1],sys.argv[2]
    print '\n'
    print complete_evaluate(sys.argv[1],sys.argv[2])