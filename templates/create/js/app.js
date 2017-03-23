function questionText () {
	return `<div class="question"">
				<div class="questionName">
					<input type="text" name="question_text" value="Введите вопрос">
					<select name="answer-type" id="answer-type">
						
					</select>
				</div>
				<div class="answersBox"></div>
				<button type="button" class="nextAnswer">Новый вариант ответа</button type="button">
			</div>`
}

function answersText() {

	return `<div class="answers">
				<input type="text" name="answer_text" value="Вариант ответа">
				<button type="button" class="delAnswer">X</button type="button">
			</div>`
}

$(document).ready(function() {
	//Добавление нового вопроса
	$(".newQuestion").click(function() {
		$(".questionBox").append(questionText());
	});
	//Добавление нового варианта ответа
    $(".content").on("click", ".nextAnswer",function() {
    	$(this).prev().append(answersText());
    });
    //Удаление варианта ответа
    $(".content").on("click", ".delAnswer" ,function() {
    	$(this).parent().remove()});
});