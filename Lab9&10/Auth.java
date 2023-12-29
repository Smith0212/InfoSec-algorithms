import java.util.Random;

class keySet{
    long e;
    long d;
    long n;
}

public class Auth {
    public static boolean isPrime(long a){
        for (int i = 2; i < (int)a/2 ; i++) {
            if(a%i == 0){
                return false;
            }
        }
        return true;
    }
    public static boolean isRelativelyPrime(long a,long b){
        long temp = a>b ? b : a;

        for (long i = 2; i <= temp; i++) {
            if(a%i==0 && b%i ==0){
                return false;
            }
        }
        return true;
    }
    public static keySet generateDE(long p,long q){
        keySet a = new keySet();
        long n = p*q;
        long totient = (p-1)*(q-1);
        long e =2;
        for (long i = 2; i < totient; i++) {
            if(isRelativelyPrime(i,totient)){
                e = i;
                break;
            }
        }
        long d =0;
        for (long i = 0; i < e; i++) {
            long temp = i * totient +1;
            if(temp%e == 0){
                d = temp/e;
                break;
            }
        }
        a.d = d;
        a.e = e;
        a.n = n;
        return a;
    }

    public static long getRandomPrime(int a){
        Random rand = new Random();
        int min = 10*4;
        String temp  = "";
        for (int i = 0; i <a ; i++) {
            temp += "9";
        }
        int max = Integer.parseInt(temp);
        int n = a;
        while (true){
            long randomNum = rand.nextInt(min,max);
            if(isPrime(randomNum)){
                return randomNum;
            }
        }
    }

    public static long powMod(long x,long y,long n){
        long power = 2;
        long finalNum = 1;
        while (power != y+1){
            if(power == 2){
                long temp = finalNum * x * x ;
                finalNum = temp % n;
            }
            else {
                long temp = finalNum * x;
                finalNum = temp % n;
            }
            power++;
        }
        return finalNum;
    }

    public static long encryption(long d,long n,long plain_txt){
//        long cipher = Math.pow(plain_txt,e) % n ;
        long cipher = powMod(plain_txt,d,n);
        return cipher;
    }

    public static long decryption(long e,long n,String appended,int len){
        long cipher = find_Ds(appended,len);
//        long plain = Math.pow(cipher,d) % n;
        long plain = powMod(cipher,e,n);
        return plain;
    }

    public static String append(long msg , long ds){
        String str = Long.toString(msg) + Long.toString(ds);
        return str;
    }

    public static long find_Ds(String appended,int len){
        String res = appended.substring(len,appended.length());
        long ds = Long.parseLong(res);
        return ds;
    }


    public static void main(String[] args) {
        long p = getRandomPrime(3);
        long q = getRandomPrime(3);
        keySet keys = generateDE(p,q);

        long msg = 19002;
        long cipher = encryption(keys.d,keys.n,msg);
        String str = append(msg,cipher);
        System.out.println("Appended string with msg and ds : " + str);
//        System.out.println("Digital Signature is -->"+cipher);
        long verifiedSign = decryption(keys.e,keys.n,str,4);
        System.out.println("Decrypted message -->"+verifiedSign);

        if(msg == verifiedSign){
            System.out.println("The user is verified as ds is correct");
        }
        else {
            System.out.println("User is not verified");
        }
    }
}