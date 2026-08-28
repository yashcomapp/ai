function createTopic(boardCode, classNum, subjectCode, chNum, topNum, name, subtopics = [], practiceSet = '', theorems = [], problemSet = '') {
  const numStr = `${chNum}.${topNum}`;
  const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chNum}-${numStr}`;
  return {
    number: numStr,
    name,
    topicCode,
    subtopics,
    practiceSet: practiceSet || `Exercise ${numStr}`,
    theorems,
    problemSet: problemSet || `Problem Set ${chNum}`
  };
}

module.exports = { createTopic };
