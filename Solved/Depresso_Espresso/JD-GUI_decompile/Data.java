import java.io.Serializable;
import javax.crypto.SealedObject;
import javax.crypto.SecretKey;

public class Data
implements Serializable {
        private final SealedObject sealed;
        private final SecretKey key;

        public Data(SealedObject paramSealedObject, SecretKey paramSecretKey) {
                this.sealed = paramSealedObject;
                this.key = paramSecretKey;
        }

        public SealedObject getSealed() {
                return this.sealed;
        }

        public SecretKey getKey() {
                return this.key;
        }
}