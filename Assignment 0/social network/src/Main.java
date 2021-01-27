public class Main {

    public static void main(String[] args) {
        
        post x = new post("hello");
        post y = x;
        x.setcontent("nbshjvccvb");
        System.out.println(x.getClass());
    }
    
}

class post{

    public String content;
    public post(String s)
    {
        this.content = s;
    }

    public void setcontent(String s)
    {
        this.content =s;
    }

    public String toString(){
        return this.content;
    }
}
