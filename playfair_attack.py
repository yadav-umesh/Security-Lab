class Playfair:

    print("enter keyword:")
    key=input()#string
    print("enter message to be enncrypted:")
    msg=input()

    pfEncryption=PFEncryption();
    pfEncryption.makeArray(key);
    msg=pfEncryption.manageMessage(msg);
    pfEncryption.doPlayFair(msg, "Encrypt");
    en=pfEncryption.getEncrypted();#string
    print("Encrypting....\n\nThe encrypted text is: " + en)
    print("=======================================")
    pfEncryption.doPlayFair(en, "Decrypt");
    print("\nDecrypting....\n\nThe encrypted text is: " + pfEncryption.getDecrypted());

class PFEncryption:
      rows,columns=(5,5)
      unique=26
      alphabets= [[0]*cols]*rows
      uniqueChar=[0 for i in range(unique)]
ch="ABCDEFGHIKLMNOPQRSTUVWXYZ";
encrypted="";
decrypted="";

def makeArray(keyword):
    keyword=keyword.toUpperCase().replace("J","I");
    present=false
    terminate=false;
    val=0
    uniqueLen;
    for i in range(0,keyword.length(),1):

        present=false;
        uniqueLen=0;
        if (keyword.charAt(i)!= ' '):
            for k in range(0, uniqueChar.length, 1):
                if (Character.toString(uniqueChar[k])==null):
                    break;
                uniqueLen+=1
            for j in range(0, uniqueChar.length, 1):
                if (keyword.charAt(i)==uniqueChar[j]):
                    present=true;
            if (present):#'!present' is correct
                uniqueChar[val]=keyword.charAt(i);
                val+=1
        ch=ch.replaceAll(Character.toString(keyword.charAt(i)), "")

    for i in range(0, ch.length, 1):
        uniqueChar[val]=ch.charAt(i);
        val+=1
    val=0;

    for i in range(0,5,1):
        for j in range(0, 5, 1):
            alphabets[i][j]=uniqueChar[val];
            val+=1
            print(alphabets[i][j] + "\t");
        println();

    def manageMessage(msg):
      val=0;
      len=msg.length()-2;
      newTxt="";
      intermediate="";
    while (len>=0):
        intermediate=msg.substring(val, val+2);
        if (intermediate.charAt(0)==intermediate.charAt(1)):
            newTxt=intermediate.charAt(0) + "x" + intermediate.charAt(1);
            msg=msg.replaceFirst(intermediate, newTxt);
            len+=1
        len-=2;
        val+=2;


    if (msg.length()%2!=0):
        msg=msg+'x';
        return msg.toUpperCase().replaceAll("J","I").replaceAll(" ","")

def doPlayFair(msg, tag):
       val=0;
       while (val<msg.length()):
         searchAndEncryptOrDecrypt(msg.substring(val, val + 2), tag);
         val+=2;


def searchAndEncryptOrDecrypt(doubblyCh,tag):
    ch1=doubblyCh.charAt(0);
    ch2=doubblyCh.charAt(1);
    row1=0
    col1=0
    row2=0
    col2=0
    for i in range(0,5,1):
        for j in range(0,5,1):
            if (alphabets[i][j]==ch1):
                row1=i;
                col1=j;
            elif (alphabets[i][j]==ch2):
                row2=i;
                col2=j;

    if (tag=="Encrypt"):
        encrypt(row1, col1, row2, col2);
    elif (tag=="Decrypt"):
        decrypt(row1, col1, row2, col2);

def encrypt(row1,col1,row2,col2):
    if (row1==row2):
        col1=col1+1;
        col2=col2+1;
        if (col1>4):
            col1=0;
        if (col2>4):
            col2=0;
        encrypted+=(Character.toString(alphabets[row1][col1])+Character.toString(alphabets[row1][col2]));
    elif(col1==col2):
        row1=row1+1;
        row2=row2+1;
        if (row1>4):
            row1=0;
        if (row2>4):
            row2=0;
        encrypted+=(Character.toString(alphabets[row1][col1])+Character.toString(alphabets[row2][col1]));
    else:
        encrypted+=(Character.toString(alphabets[row1][col2])+Character.toString(alphabets[row2][col1]));

def decrypt(row1, col1, row2, col2):
    if (row1==row2):
        col1=col1-1;
        col2=col2-1;
        if (col1<0):
            col1=4;
        if (col2<0):
            col2=4;
        decrypted+=(Character.toString(alphabets[row1][col1])+Character.toString(alphabets[row1][col2]));
    elif(col1==col2):
        row1=row1-1;
        row2=row2-1;
        if (row1<0):
            row1=4;
        if (row2<0):
            row2=4;
        decrypted+=(Character.toString(alphabets[row1][col1])+Character.toString(alphabets[row2][col1]))
    else:
        decrypted+=(Character.toString(alphabets[row1][col2])+Character.toString(alphabets[row2][col1]))

def getEncrypted():
      return encrypted;

def getDecrypted():
    return decrypted
