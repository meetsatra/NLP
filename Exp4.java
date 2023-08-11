import org.tartarus.snowball.ext.EnglishStemmer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Exp4 {
    public static void main(String[] args) {
        String word = "running"; // Example word
        String stemmedWord = stemWord(word); // Apply Porter stemming
        Map<Integer, List<String>> wordInfoMap = createWordInfoMap();

        if (wordInfoMap.containsKey(stemmedWord.hashCode())) {
            List<String> wordInfo = wordInfoMap.get(stemmedWord.hashCode());
            System.out.println("Original Word: " + word);
            System.out.println("Stemmed Word: " + stemmedWord);
            System.out.println("Parts of Speech: " + wordInfo.get(0));
            System.out.println("Gender: " + wordInfo.get(1));
            System.out.println("Plural: " + wordInfo.get(2));
            System.out.println("Tense: " + wordInfo.get(3));
        } else {
            System.out.println("Word not found in the dictionary.");
        }
    }

    public static Map<Integer, List<String>> createWordInfoMap() {
        Map<Integer, List<String>> wordInfoMap = new HashMap<>();

        // Adding stemmed word information to the map
        wordInfoMap.put("run".hashCode(), createWordInfo("verb", "neutral", "no", "present"));
        wordInfoMap.put("eat".hashCode(), createWordInfo("verb", "neutral", "no", "present"));
        wordInfoMap.put("book".hashCode(), createWordInfo("noun", "neutral", "yes", ""));
        wordInfoMap.put("happi".hashCode(), createWordInfo("adjective", "neutral", "no", ""));
        wordInfoMap.put("jump".hashCode(), createWordInfo("verb", "neutral", "no", "present"));

        return wordInfoMap;
    }

    public static List<String> createWordInfo(String partOfSpeech, String gender, String plural, String tense) {
        List<String> wordInfo = new ArrayList<>();
        wordInfo.add(partOfSpeech);
        wordInfo.add(gender);
        wordInfo.add(plural);
        wordInfo.add(tense);
        return wordInfo;
    }

    public static String stemWord(String word) {
        EnglishStemmer stemmer = new EnglishStemmer();
        stemmer.setCurrent(word);
        stemmer.stem();
        return stemmer.getCurrent();
    }
}