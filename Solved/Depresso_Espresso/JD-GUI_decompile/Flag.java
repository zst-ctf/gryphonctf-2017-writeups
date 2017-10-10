import java.io.Serializable;

public class Flag
implements Serializable {
        private final String flag;

        public Flag(String paramString) {
                this.flag = paramString;
        }

        public String getFlag() {
                return this.flag;
        }
}
