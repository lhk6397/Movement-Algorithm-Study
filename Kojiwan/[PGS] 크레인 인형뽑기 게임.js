// https://programmers.co.kr/learn/courses/30/lessons/64061

class Stack {
  constructor() {
    this.arr = [];
    this.peek = 0;
  }
  push(item) {
    this.arr[this.peek++] = item;
  }
  pop() {
    if (this.index <= 0) return null;
    const result = this.arr[--this.peek];
    this.arr.pop();
    return result;
  }
  top() {
    if (this.peek <= 0) return null;
    return this.arr[this.peek - 1];
  }
}

function solution(board, moves) {
  var removeCount = 0;
  var item = 0;
  const basket = new Stack();
  moves.forEach((element) => {
    item = 0;
    for (let row = 0; row < board.length; row++) {
      if (board[row][element - 1] === 0) continue;
      else {
        item = board[row][element - 1];
        board[row][element - 1] = 0;
        break;
      }
    }
    if (item === basket.top()) {
      basket.pop();
      removeCount += 2;
    } else if (item !== 0) {
      basket.push(item);
    }
  });
  return removeCount;
}
