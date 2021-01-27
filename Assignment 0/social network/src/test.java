import java.util.*;

class post {
    public String content;

    public post(String s)
    {
        this.content = s;
    }

    public String toString()
    {
        return content;
    }
}

public class test {
    
    public ArrayList<post> contents = new ArrayList<post>();

    public test() {

        String s = "hello world";
        contents.add(new post(s));

    }

    public void changecontent(int i, String s)
    {
        contents.get(i).content = s;
    }

    public static void main(String[] args) {

        test obj = new test();

        post s = obj.contents.get(0);

        obj.changecontent(0, "lol");

        System.out.println(s);

        String change = "blabla";

        obj.changecontent(0, change);

        
        System.out.println(s);

    }
    
}
