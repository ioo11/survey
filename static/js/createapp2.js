function questionText (ID) {
	return `<div class="question" id="${ID}">
				<div class="questionName">
					<input type="text" name="question_text" value="Введите вопрос">
				</div>
				<div class="answersBox"></div>
				<button type="button" class="nextAnswer">Новый вариант ответа</button type="button">
			</div>`
}

function answersText(ID) {
	return `<div class="answers" id="${ID}">
				<input type="text" name="answer_text" value="Вариант ответа">
				<button type="button" class="delAnswer">X</button type="button">
			</div>`
}

let added_question = 0;
let added_answer = [];

$(document).ready(function() {
	//Добавление нового вопроса
	$(".newQuestion").click(function() {
		$(".questionBox").append(questionText(added_question));
		added_answer[added_question] = 0;
		added_question++
	});
	//Добавление нового варианта ответа
    $(".content").on("click", ".nextAnswer",function() {
    	let j = $(this).prev();
    	let questionId = j.parent('.question').attr('id');
    	j.append(answersText(questionId + '.' + added_answer[questionId]++));
    });
    //Удаление варианта ответа
    $(".content").on("click", ".delAnswer" ,function() {
    	$(this).parent().remove()});
});
