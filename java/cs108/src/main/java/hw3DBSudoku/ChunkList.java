import java.util.*;

public class ChunkList<E> extends AbstractCollection<E> {

    public ChunkList() {

    }

    public void clear() {

    }

    public Iterator<E> iterator() {
        return new ChunkListIterator<E>();
    }

    public int size() {
        return 0;
    }
}