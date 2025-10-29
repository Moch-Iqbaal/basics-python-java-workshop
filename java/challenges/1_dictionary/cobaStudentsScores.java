import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class cobaStudentsScores {
    public static void main (String [] args) {
        Scanner inputScanner = new Scanner(System.in);
        Map<String, Integer> scores = new HashMap<>();

        while (true) {
            System.out.print("Masukkan nama anda atau ENTER untuk selesai: ");
            String nama = inputScanner.nextLine().trim();
            if (nama.isEmpty()) break;

            int nilai = 0;
            while (true) {
                System.out.print("Masukka nilai AndaL: ");
                String input = inputScanner.nextLine().trim();
                try{
                    nilai = Integer.parseInt(input);
                    break;
                }catch(NumberFormatException e){
                    System.out.println("Nilai harus angka!");
                }
            }

            scores.put(nama, nilai);

            // menampilkna hasilnya
            System.out.println("\n Daftar nilai siswa: ");
            for (Map.Entry<String, Integer> entry : scores.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        }   
        inputScanner.close();
    }
}