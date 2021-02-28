
fun name(Myname:String):String{
    return Myname
}

fun remainder(a:Int,b:Int):Int{
    return a%b
}
fun Add(x:Int,y:Int,z:Int,m:Int):Int{
    return x+y+z+m
}
fun InterstingFact(MyinterestingFact:String):String{
    return MyinterestingFact
}
fun main() {
    var Myname = name("Hello Chantal")
    var rem = remainder(30, 4)
    var sum = Add(20, 10, 20, 40)
    var MyinterestingFact = InterstingFact("My perfect day starts and ends with a prayer")
    println(Myname)
    println(rem)
    println(sum)
    println(MyinterestingFact)
}