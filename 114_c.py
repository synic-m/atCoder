N = int(input())
stage = []

def dfs(s):
    if int(s) > N:
        return 0 #Nを超えたら処理終了
    ret  = 1 if all(s.count(c) > 0 for c in '753') else 0
    #753がすべて1個以上あるかのチェック あれば+1をする
    #retは答えになる変数＋＝1みたいなイメージ
    #allはすべてTrueならばTrueをかえす
    #Trueならば１Falseならば０を返す
    for c in '753': #c 753を繰り返す
        ret += dfs(s+c)#str でｃの値を受け取ったｓに加えてdfsに再起処理をする
    return ret
print(dfs('0'))



#forの深さが変数の数に応じて増えるならば再帰を考える
#
