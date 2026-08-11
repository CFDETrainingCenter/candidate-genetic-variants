function showKnowledgeFeedback(feedback, status, label, message) {
  const strongLabel = document.createElement("strong");
  strongLabel.textContent = label;

  feedback.replaceChildren(strongLabel, document.createTextNode(` ${message}`));
  feedback.classList.remove("correct", "incorrect");
  feedback.classList.add(status);
  feedback.hidden = false;
}

function initializeKnowledgeCheck(knowledgeCheck) {
  const submitButton = knowledgeCheck.querySelector(".knowledge-submit");
  const feedback = knowledgeCheck.querySelector(".knowledge-feedback");
  const answerInputs = knowledgeCheck.querySelectorAll('input[type="radio"]');

  if (!submitButton || !feedback || answerInputs.length === 0) {
    return;
  }

  answerInputs.forEach((answerInput) => {
    answerInput.addEventListener("change", () => {
      // Hide old feedback when the learner changes the selected answer.
      feedback.hidden = true;
      feedback.classList.remove("correct", "incorrect");
    });
  });

  submitButton.addEventListener("click", () => {
    const selectedAnswer = knowledgeCheck.querySelector(
      'input[type="radio"]:checked',
    );

    if (!selectedAnswer) {
      showKnowledgeFeedback(
        feedback,
        "incorrect",
        "Choose an answer.",
        "Select one option before you submit.",
      );
      return;
    }

    const isCorrect = selectedAnswer.value === knowledgeCheck.dataset.answer;
    if (isCorrect) {
      showKnowledgeFeedback(
        feedback,
        "correct",
        "Correct.",
        knowledgeCheck.dataset.correct,
      );
      return;
    }

    showKnowledgeFeedback(
      feedback,
      "incorrect",
      "Try again.",
      knowledgeCheck.dataset.incorrect,
    );
  });
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".knowledge-check").forEach(initializeKnowledgeCheck);
});
