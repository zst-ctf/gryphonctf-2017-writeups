import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SealedObject;
import javax.crypto.SecretKey;
import java.io.*;
import java.util.*;

public class GetKey {
    public static void main(String[] args) throws Exception {     
        // Read in the serialisable object   
        File file = new File("output.bin");
        FileInputStream fis = new FileInputStream(file);
        ObjectInputStream in = new ObjectInputStream(fis);
        Object obj = in.readObject(); 

        // Extract out the key and sealed object
        Data data = (Data) obj;
        SecretKey localSecretKey = data.getKey();
        SealedObject localSealedObject = data.getSealed();

        // Get flag from sealed object
        Object flag_obj = localSealedObject.getObject(localSecretKey);
        Flag flag = (Flag) flag_obj;

        System.out.println("This is the flag:");
        System.out.println(flag.getFlag());
    }
}
