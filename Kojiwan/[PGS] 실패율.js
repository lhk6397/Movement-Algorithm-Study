// https://programmers.co.kr/learn/courses/30/lessons/42889

function solution(N, stages) {
  var answer = [];
  var tempArr = [];

  for (let targetStage = 1; targetStage <= N; ++targetStage) {
    const userNum = stages.filter((stage) => stage >= targetStage).length;
    const count = stages.filter((nowStage) => targetStage === nowStage).length;
    const failure = count / userNum;
    const stageInfo = { index: targetStage, failure: failure };
    tempArr.push(stageInfo);
  }

  tempArr.sort((a, b) => {
    return b.failure - a.failure;
  });

  for (let i = 0; i < tempArr.length; ++i) {
    answer.push(tempArr[i].index);
  }

  return answer;
}

solution(4, [4, 4, 4, 4, 4]);
