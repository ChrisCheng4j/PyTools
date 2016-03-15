package <your package>;

import android.content.pm.ApplicationInfo;

import java.io.IOException;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class ChannelConfig {

    private static final String DEFAULT_CHANNEL = "";
    private static final String PREFIX = "channel";
    private static final String EXPRESSION = "_";

    public static String getChannel() {
        ApplicationInfo info = <your application context>.getApplicationInfo();
        String sourceDir = info.sourceDir;

        ZipFile zipFile = null;
        try {
            zipFile = new ZipFile(sourceDir);
            Enumeration entries = zipFile.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = (ZipEntry) entries.nextElement();
                String entryName = entry.getName();
                if (entryName.startsWith(PREFIX)) {
                    String[] split = entryName.split(EXPRESSION);
                    if (split != null && split.length >= 2)
                        return entryName.substring(split[0].length() + 1);
                    else
                        return DEFAULT_CHANNEL;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (zipFile != null) {
                try {
                    zipFile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        return DEFAULT_CHANNEL;
    }
}
