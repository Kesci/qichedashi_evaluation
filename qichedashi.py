import sys
import pandas as pd
import numpy as np

def normalize(s):
    """
    Normalize strings to space joined chars.

    Args:
        s: a list of strings.

    Returns:
        A list of normalized strings.
    """
    if not s:
        return s
    normalized = []
    for ss in s:
        tokens = [c for c in list(ss) if len(c.strip()) != 0]
        normalized.append(' '.join(tokens))
    return normalized

def my_lcs(string, sub):
    if len(string) < len(sub):
        sub, string = string, sub
    lengths = [[0 for i in range(0,len(sub)+1)] for j in range(0,len(string)+1)]

    for j in range(1,len(sub)+1):
        for i in range(1,len(string)+1):
            if(string[i-1] == sub[j-1]):
                lengths[i][j] = lengths[i-1][j-1] + 1
            else:
                lengths[i][j] = max(lengths[i-1][j] , lengths[i][j-1])

    return lengths[len(string)][len(sub)]


def calc_score(candidate, refs):

    beta = 1.2

    candidate = normalize(candidate)
    refs = normalize(refs)

    assert(len(candidate)==1)
    assert(len(refs)==1)

    prec = []
    rec = []

    token_c = candidate[0].split(" ")

    for reference in refs:
        token_r = reference.split(" ")
        lcs = my_lcs(token_r, token_c)
        prec.append(lcs/float(len(token_c)))
        rec.append(lcs/float(len(token_r)))

    prec_max = max(prec)
    rec_max = max(rec)

    if (prec_max!=0 and rec_max!=0):
        score = ((1 + beta**2)*prec_max*rec_max)/float(rec_max + beta**2*prec_max)
    else:
        score = 0.0

    return score


def validate(submit_file, test_file, options):

    submission = pd.read_csv(submit_file, dtype={'QID': str, 'Prediction': str})

    groundtruth = pd.read_csv(test_file, dtype={'QID': str, 'Report': str})

    if len(submission['QID'].unique()) != len(groundtruth['QID'].index):
        raise Exception('预测结果中没有全部答案ID')

    if len(np.intersect1d(submission['QID'], groundtruth['QID'])) <= 0:
        raise Exception('No ID matches')
    
    if sorted(submission['QID'].unique()) != sorted(groundtruth['QID'].unique()):
        raise Exception('Loss of submission IDs')
        
    return {
        "code": 0,
        "message": 'Validation Success',
    }


def score(submit_file, test_file, options):
    submission = pd.read_csv(submit_file, dtype={'QID': str, 'Prediction': str}, index_col=False)

    groundtruth = pd.read_csv(test_file, dtype={'QID': str, 'Report': str}, index_col=False)

    tmp = pd.merge(submission, groundtruth, on='QID', how='inner')
    if list(tmp.columns) != ['QID', 'Prediction','Report']:
        raise 'column name is wrong'

    score = []

    for submit, answer in zip(tmp['Prediction'],tmp['Report']):
        sc = calc_score([submit],[answer])
        score.append(sc)
    
    final_score = round(np.mean(score) * 100,4)

    return {
        "code": 0,
        "score": final_score,
        "message": "success"
    }







if __name__ == '__main__':
    
    submit_file = sys.argv[1]
    test_file = sys.argv[2]

    print (validate(submit_file,test_file,options=True))
    print (score(submit_file,test_file,options=True))



