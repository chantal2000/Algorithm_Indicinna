fun main() {
    add()
    Love()
    var fname="Niyonkuru"
    var age=29
    val lname="Niyonkuru Marie Chantal"
    val weight=49.4
    println(fname[2])
    println(fname[3])
    println(fname.toLowerCase())
    println(fname.toUpperCase())
    println(fname.capitalize())
    println(fname  + " is " + age)
    println(lname.trimStart())
    println(lname.trimEnd())
    println(lname.replace("Marie","Chantal"))
    println(fname + age + lname)
    println("weight is" + weight.toString())
    println(fname.endsWith("u"))
    println(fname.isEmpty())
    println(fname.isBlank())
    println(lname.trim())

}
fun add(){
    var X=30
    var Y=20
    var sum=X+Y
    println(sum)
}
fun Love(){
    var fname="Mum"
    var lname="Dad"
    println(fname)
    println(lname)
}