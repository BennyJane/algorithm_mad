

/*
* 使用split将字符分开后，要么得到空格，要么得到字符，要么得到..或是.
使用栈模拟，遍历字符数组，如果是正常字符，就栈入，如果是..则弹出，如果是.或是空则continue
最后遍历栈，将字符拼接在一起返回即可
*/
class Solution {
    public String simplifyPath(String path) {
        String[] pathArray = path.split("/");
        //分割后的几种情况 空格说明是多出来的/，.. .与目录
        StringBuilder res =new StringBuilder();
        Deque<String> stack = new ArrayDeque<>();
        for(int i=0;i<pathArray.length;i++){
            //2种情况，栈为空或者栈不为空
            if(pathArray[i].length()==0||pathArray[i].equals("."))    continue;
            if(!stack.isEmpty()){
                if(pathArray[i].equals("..")){
                    stack.pop();
                }else{
                    stack.push(pathArray[i]);
                }
            }else{
                if(!pathArray[i].equals(".."))  stack.push(pathArray[i]);
            }
        }
        if(stack.isEmpty())    return res.append('/').toString();
        while(!stack.isEmpty()){
            res.insert(0,stack.pop());
            res.insert(0,'/');
        }
        return res.toString();
    }
}

