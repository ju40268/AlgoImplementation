public class Vector2D implements Iterator<Integer> {
    int indexList, indexElement;
    public List<List<Integer>> flatten;

    public Vector2D(List<List<Integer>> vec2d) {
        indexList = 0;
        indexElement = 0;
        flatten = vec2d;      
    }

    @Override
    public Integer next() {
        return flatten.get(indexList).get(indexElement++);      
    }

    @Override
    public boolean hasNext() {
        while (indexList < flatten.size()){
            if (indexElement < flatten.get(indexList).size()) return true;
            else{
                indexList++;
                indexElement = 0;
            }
        }
        return false;
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */