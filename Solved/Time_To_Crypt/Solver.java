package Time_to_Crypt;

import java.io.*;
import java.util.*;
import java.util.Arrays;
import Time_to_Crypt.OTP.Data;
import static Time_to_Crypt.OTP.encrypt;

public class Solver {

    public static void main(String[] args) throws Exception {
        String text = "Congratulations! Here is the flag!";
        
        File file = new File("./Time_to_Crypt/output");
        FileInputStream fis = new FileInputStream(file);
        ObjectInputStream in = new ObjectInputStream(fis);
        Object obj = in.readObject(); 

        Data data = (Data) obj;

        byte[] text_enc = data.getData1();
        byte[] key = encrypt(text_enc, text.getBytes());

        byte[] flag_enc = data.getData2();
        byte[] flag = encrypt(flag_enc, key);

        System.out.println("FLAG: " + new String(flag));
    }


}
