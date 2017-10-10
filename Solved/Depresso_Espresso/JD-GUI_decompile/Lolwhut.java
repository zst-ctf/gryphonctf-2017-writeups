import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.PrintStream;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SealedObject;
import javax.crypto.SecretKey;

public class Lolwhut {
		public static void main(String[] paramArrayOfString)
		throws Exception {
				if (paramArrayOfString.length != 4) {
						System.out.println("Lolwhut <algorithm> <cipher mode> <flag> <output file>");
						return;
				}
				KeyGenerator localKeyGenerator = KeyGenerator.getInstance(paramArrayOfString[0]);
				SecretKey localSecretKey = localKeyGenerator.generateKey();
				Cipher localCipher = Cipher.getInstance(paramArrayOfString[1]);
				localCipher.init(1, localSecretKey);
				SealedObject localSealedObject = new SealedObject(new Flag(paramArrayOfString[2]), localCipher);
				Data localData = new Data(localSealedObject, localSecretKey);
				FileOutputStream localFileOutputStream = new FileOutputStream(paramArrayOfString[3]);
				ObjectOutputStream localObjectOutputStream = new ObjectOutputStream(localFileOutputStream);
				localObjectOutputStream.writeObject(localData);
				localObjectOutputStream.close();
				System.out.println("File " + paramArrayOfString[3] + " created");
		}
}
