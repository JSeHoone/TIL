import java.sql.SQLOutput;
import java.util.HashMap;
import java.util.Objects;

public class HashMapExample {

    /*
    * HashMap에서 2의 제곱수로 capacity를 쓰는 이유
    * - 비트 연산 최적화 때문이다
    * - % 연산자보다 &연산이 CPU에서 더 저렴하다
    *
    * 2의 제곱수가 아닐 때
    * - 특정 Bucket에 데이터가 몰리게 된다.
    *
    * 2의 제곱수가 잘 분산되는 이유는 모든 하위 비트를 사용하기 때문이다
    * 그래서 HashMap내부에 tableSizeFor(cap)이라는 함수가 존재하는데, 이 함수가 2의 제곱수로 변환해준다
    *
    * */
//    public static void main(String[] args) {
//
//        // new로 hashmap을 생성했다고 하더라도 배열을 바로 생성되지 않는다 (lazy initialization)
//        HashMap<String, Integer> map = new HashMap<>();
//
//        // 이때, 배열이 생성 된다.(put 할 때) -> 내부 배열의 크기는 16이다.
//        map.put("apple",100);
//
//        // "apple"을 해시코드로 변환
//        int hashCodeNumber = "apple".hashCode();
//        System.out.println(hashCodeNumber);
//
//        // index 계산 (hash % 배열의 크기)
//        // % 연산자를 쓰지 않고 & 연산자를 쓰는 이유는 CPU에서 더 빠르기 때문이다.
//        // 그래서 HashMap에서는 항상 2의 제곱수를 유지한다 (16, 32, 64 ...)
//        int index = (16 - 1) & hashCodeNumber;
//        System.out.println(index);
//    }

    /*
    * 2의 제곱수를 사용하더라도 Collision(해시 충돌)이 발생할 수 있다.
    *
    * HashMap의 흐름: key -> hashCode() -> hash mixing -> index 계산 -> bucket 위치
    * 여기서 문제는 무한한 key, 유한한 bucket이라는 점이다.
    *
    * bucket size를 16으로 하면 index는 0 ~ 15밖에 되지 않는다.
    * 그런데, key는 무한대이므로 다른 key -> 같은 bucket이 되는 건 필연적이다.
    * 이걸 collision이라고 한다.
    * */
    public static void main(String[] args) {
        // Collision 예제 (동일한 hashCode를 가진다)
        System.out.println("FB".hashCode());
        System.out.println("Ea".hashCode());

        // Java 7이전에는 Separate Chaining으로 이 문제를 해결했다
        /*
        * bucket[3]
        * -> FB
        * -> Ea
        * -> Apple
        * */
        // bucket 내부가 배열로 되어있고, 이를 equals()로 비교해서 찾을 때 까지 순회한다.
        // 기본적으로 O(1)이지만 collision이 심하면 O(n)까지 된다.

        // Java 8부터는 이를 개선했는데, 충돌이 많아지면 linked list -> Red-Black Tree로 변환한다.
        /*
        *       bucket[3]
                  ↓
                 Tree
               /     \
            node     node
        * */

        // 이렇게 변환되는 조건이 있는데,
        // bucket node >= 8 & capacity >= 64 이면 Tree화를 진행한다
        // 그래서 최악의 경우 O(log n)이 된다.


        // Collision 예방 방법 1 - 좋은 hashCode 만들기 (분산이 좋아지게 만들기)
        // @Override
        // public int hashCode() {
        //     return Objects.hash(id,name);
        // }

        // Collision 예방 방법 2 - 적절한 initial capacity 지정
        // new HashMap<>(); 을 쓰면 resize가 엄청 발생한다.
        // new HashMap<>(164384); 처럼 미리 설정해둔다


        // Collision 예방 방법 3 - load factor 이해
        // load factor가 0.75가 기본인데, ( 16 x 0.75 = 12)
        // 12개가 넘으면 resize가 발생한다.
        // 왜 발생하냐면 bucket의 밀도를 방지하고 collision을 줄이기 위해서다.


    }


}
