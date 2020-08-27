package baekJoon_10971;
import java.util.Scanner;

public class BaekJoon_Test {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //���ð� �̵� ��� ��� W
        int[][] W;

        //�̵� ��� ������ ����
        int result=0;

        //���� ���� N�Է� (2<= N <=10)
        int N = sc.nextInt();

        //���  W�Է¹ޱ�
        W=new int[N][N];
        for (int i = 0; i < W.length; i++) {
            for (int j = 0; j < W[0].length; j++) {
                W[i][j]=sc.nextInt();
            }
        }

        //��ȴ� �������� Ȯ���ϴ� �迭
        int[] visit = new int[N];
        visit[0]=1;
        int a = 0;
        for (int i = 0; i < N; i++) {
            int tmp = 0;
            for (int j = 0; j < N; j++) {
                if(visit[j]==1) {continue;}
                else if(W[a][j]==0) {continue;}
                visit[j]=1;
                tmp+=W[a][j];
                if(tmp>=result) {
                    result = tmp;
                }
                a=j;
            }
        }

        System.out.println("�ּҰ� : "+result);



    }

}
