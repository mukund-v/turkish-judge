
def example_answer():
    return """
    <?xml version="1.0" encoding="ASCII"?><QuestionFormAnswers xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd">
    <Answer><QuestionIdentifier>1.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>1.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>1.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>2.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>2.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>2.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>3.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>3.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>3.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>4.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>4.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>4.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>5.BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>5.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>5.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>6.BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>6.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>6.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>7.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>7.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>7.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>8.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>8.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>8.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>9.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer>
    <Answer><QuestionIdentifier>9.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer>
    <Answer><QuestionIdentifier>9.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>10.BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>10.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>10.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>11.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>11.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>11.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>12.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>12.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>12.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>13.BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>13.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>13.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>14.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>14.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>14.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>15.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>15.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>15.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>16.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>16.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>16.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>17.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>17.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>17.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>18.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>18.NOT BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>18.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>19.BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer><Answer><QuestionIdentifier>19.NOT BREAKDOWN</QuestionIdentifier><FreeText>true</FreeText></Answer><Answer><QuestionIdentifier>19.POSSIBLE BREAKDOWN</QuestionIdentifier><FreeText>false</FreeText></Answer></QuestionFormAnswers>
    """


def example_question():
    return """
    <HTMLQuestion xmlns=http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
<HTMLContent><![CDATA[

<!-- YOUR HTML BEGINS -->
<!DOCTYPE html>
<!-- You must include this JavaScript file -->
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<!-- HIT template: Survey-v3.0 --><!-- The following snippet enables the 'responsive' behavior on smaller screens -->
<crowd-form answer-format="flatten-objects">
<meta content="width=device-width,initial-scale=1" name="viewport" />
<section class="container" id="Survey"><!-- Instructions -->
<div class="row">
<div class="col-xs-12 col-md-12">
<div class="panel panel-primary"><!-- WARNING: the ids "collapseTrigger" and "instructionBody" are being used to enable expand/collapse feature --><a class="panel-heading" href="javascript:void(0);" id="collapseTrigger"><strong>Instructions</strong> <span class="collapse-text">(Click to Collapse)</span> </a>
<div class="panel-body" id="instructionBody">
<h3>Overview</h3>

<p style="margin-bottom: 15px; font-size: 16px; line-height: 1.72222; color: rgb(52, 73, 94); font-family: Lato, Helvetica, Arial, sans-serif;">In this job, you will be presented with conversations between two interalocutors (a conversational system S and a user U). Review the conversation to determine whether the last utterance by S causes a breakdown in the conversation or not.</p>

<p style="margin-bottom: 15px; font-size: 16px; line-height: 1.72222; color: rgb(52, 73, 94); font-family: Lato, Helvetica, Arial, sans-serif;"><span style="color: rgb(209, 72, 65);">This task requires native English skills.<br />
Please refrain from joining this task if you are a non-native speaker of English.</span></p>

<h3>Step</h3>

<ol style="margin-bottom: 15px; font-size: 15px; color: rgb(52, 73, 94); font-family: Lato, Helvetica, Arial, sans-serif;">
	<li>Read the conversation.</li>
	<li>Determine if the last utterance causes a breakdown in the conversation.</li>
</ol>

<h3>Rules & Tips</h3>

<p style="margin-bottom: 15px; font-size: 16px; line-height: 1.72222; color: rgb(52, 73, 94); font-family: Lato, Helvetica, Arial, sans-serif;">For the last utterance of each conversation, you will choose BREAKDOWN, POSSIBLE BREAKDOWN, or NOT A BREAKDOWN:</p>

<p><span style="color: rgb(52, 73, 94); font-family: Lato, Helvetica, Arial, sans-serif; font-size: 16px;">The key notion is 'difficulty in continuing the conversation smoothly'.</span></p>

<table class="table table-condensed table-striped table-responsive">
	<tbody>
	</tbody>
	<colgroup>
		<col class="col-xs-2 col-md-2" />
		<col class="col-xs-10 col-md-10" />
	</colgroup>
	<!-- By explaining the sentiment scale, the accuracy of the answers may increase. -->
	<tbody>
		<tr>
			<th>Label</th>
			<th>Guidance</th>
		</tr>
		<tr>
			<td>NOT A BREAKDOWN</td>
			<td>means that it is easy to continue the conversation after the utterance in question.</td>
		</tr>
		<tr>
			<td>POSSIBLE BREAKDOWN</td>
			<td>means that it is difficult to continue the conversation smoothly after the utterance in question.</td>
		</tr>
		<tr>
			<td>BREAKDOWN</td>
			<td>means that it is difficult to continue the conversation after the utterance in question.</td>
		</tr>
	</tbody>
</table>

<h4>&nbsp;Note:</h4>

<p>Consider not only the preceding utterance but also all the given history utterances if exist for making your judgment. There are no objective and concrete criteria to choose between BREAKDOWN, POSSIBLY, and NOT A BREAKDOWN. It is okay to be subjective in making decisions.</p>

<p>Note that emojis are replaced with alternative texts (e.g.,[SMILE])</p>


<h3>Example</h3>

<table class="table table-condensed table-striped table-responsive">
	<tbody>
	</tbody>
	<colgroup>
		<col class="col-xs-8 col-md-8" />
		<col class="col-xs-4 col-md-4" />
	</colgroup>
	<!-- By explaining the sentiment scale, the accuracy of the answers may increase. -->
	<tbody>
		<tr>
			<td>
			<p>NOT A BREAKDOWN</p>

			<p>In this example, the last utterance is a suitable response to a greeting. So, this is not a breakdown.</p>
			</td>
			<td>​U: How are you?<br />
			S: Fine. How about you?</td>
		</tr>
		<tr>
			<td>
			<p>POSSIBLE BREAKDOWN</p>

			<p>​In this example, the last utterance is socially awkward. So this can be labeled a possible breakdown.</p>
			</td>
			<td>U: How are you?<br />
			S: Does it matter?</td>
		</tr>
		<tr>
			<td>
			<p>BREAKDOWN</p>

			<p>In this example, the last utterance does not make any sense. So, &nbsp;this will be given a breakdown label.</p>
			</td>
			<td>
			<p>U: How are you?<br />
			S: I am a green fire of fish.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>BREAKDOWN</p>

			<div>In this example, the last utterance is not answering the question at all.</div>
			</td>
			<td>U: What is your hobby, then?<br />
			S: When was your last trip?</td>
		</tr>
		<tr>
			<td>
			<p>BREAKDOWN</p>

			<div>In this example, the last utterance is inconsistent with the first utterance.</div>
			</td>
			<td>S: It's nice to go shopping alone.<br />
			U: I agree. That's nice.<br />
			S: Shopping takes time.<br />
			U: Window shopping is also fun.<br />
			S: It's fun to go shopping with somebody.</td>
		</tr>
	</tbody>
</table>
</div>
</div>
</div>
</div>
<!-- End Instructions --><!-- Survey Layout -->

<div class="row" id="workContent" name="${dialogid}">
<div class="col-sm-8 col-sm-offset-2">
<p style="margin-bottom: 15px; font-size: 16px; line-height: 1.72222; color: rgb(52, 73, 94); font-family: Lato, Helvetica, Arial, sans-serif;"><span style="color: rgb(209, 72, 65);">The result may not be approved if it is considered as cheating by checking utterances which consist of Obviously BREAKDOWN and NOT A BREAKDOWN utterances. </span></p>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="1" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="1" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="1" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="2" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="2" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="2" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="3" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="3" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="3" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="4" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="4" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="4" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="5" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="5" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="5" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="6" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="6" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="6" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="7" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="7" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="7" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="8" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="8" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="8" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="9" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="9" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="9" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="10" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="10" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="10" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="11" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="11" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="11" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
<br>U: a girl likes me. what do i do
<br>S: do you want to hear some latest football news?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="12" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="12" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="12" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
<br>U: a girl likes me. what do i do
<br>S: do you want to hear some latest football news?
<br>U: no
<br>S: okay, let's keep talking about football. who is your favorite football player?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="13" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="13" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="13" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
<br>U: a girl likes me. what do i do
<br>S: do you want to hear some latest football news?
<br>U: no
<br>S: okay, let's keep talking about football. who is your favorite football player?
<br>U: talk to me about girls
<br>S: that's cool. personally i think, my favorite player is tom brady. there are many people who dislike him, but i think his skills and championship mentality are incredible.
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="14" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="14" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="14" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
<br>U: a girl likes me. what do i do
<br>S: do you want to hear some latest football news?
<br>U: no
<br>S: okay, let's keep talking about football. who is your favorite football player?
<br>U: talk to me about girls
<br>S: that's cool. personally i think, my favorite player is tom brady. there are many people who dislike him, but i think his skills and championship mentality are incredible.
<br>U: stop talking about football
<br>S: thanks for chatting. if you want to exit social mode, just say stop.
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="15" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="15" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="15" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
<br>U: a girl likes me. what do i do
<br>S: do you want to hear some latest football news?
<br>U: no
<br>S: okay, let's keep talking about football. who is your favorite football player?
<br>U: talk to me about girls
<br>S: that's cool. personally i think, my favorite player is tom brady. there are many people who dislike him, but i think his skills and championship mentality are incredible.
<br>U: stop talking about football
<br>S: thanks for chatting. if you want to exit social mode, just say stop.
<br>U: what do you think about girls
<br>S: i don't have an answer for this question. do you mind telling me what you think?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="16" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="16" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="16" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>

    <div class="panel panel-default">
    <div class="panel-body"><label><font color = "black">Read the text below paying close attention to detail, especially to the last utterances:</label>

    <p class="well">S: hi, this is an alexa prize socialbot. nice to meet you! do you want to tell me your name?
<br>U: ted
<br>S: hi, ted. i can talk about movies, books and animals. i can even tell you about some obscure holidays. what do you want to talk about?
<br>U: what do you like to do in your free time
<br>S: i like to chat with you!
<br>U: okay. you start talking
<br>S: <say-as interpret-as="interjection"> all righty!</say-as>. what else are you interested in? have you seen any good movies recently?
<br>U: i is the netflix series called a sample. what's your list pretty cool
<br>S: <prosody rate = "60%">so</prosody> <break time = "300ms"></break> what else are you interested in? do you like to read a lot of books?
<br>U: i wish. but i don't have the patience
<br>S: <say-as interpret-as="interjection">spoiler alert!!</say-as>did you know? i am definitely more of a dog bot than a cat bot. how about you? do you like animals?
<br>U: yes. but i can't have one sister live in apartment
<br>S: <prosody rate = "60%">umm</prosody><break time = "200ms"></break> <prosody rate = "70%">so,</prosody> did you know? even though i can't play sports, i enjoy watching them! how about you? are you interested in sports?
<br>U: yes
<br>S: i like watching hockey! what is your favorite team in the nhl?
<br>U: i watch football
<br>S: okay. football is one of my favorite sports. besides your favorite team, which teams do you think are the favorites for super bowl 2019?
<br>U: cowboys and redskins
<br>S: nice, cowboys and redskins is a good choice! i found something interesting on cowboys and redskins.: the cowboys-redskins nfl rivalry started when the owner of the cowboys bought the redskins fight song and held it hostage to get voted into the nfl.. isn't this interesting?
<br>U: kinda
<br>S: okay, let's keep talking about football. what is your favorite part when you watch a football game?
<br>U: long pass
<br>S: ok. in my opinion, collecting players data and analyzing their performance is my favoriate thing to do when i watch a football game.
<br>U: a girl likes me. what do i do
<br>S: do you want to hear some latest football news?
<br>U: no
<br>S: okay, let's keep talking about football. who is your favorite football player?
<br>U: talk to me about girls
<br>S: that's cool. personally i think, my favorite player is tom brady. there are many people who dislike him, but i think his skills and championship mentality are incredible.
<br>U: stop talking about football
<br>S: thanks for chatting. if you want to exit social mode, just say stop.
<br>U: what do you think about girls
<br>S: i don't have an answer for this question. do you mind telling me what you think?
<br>U: i'm thinking that i need to meet girls
<br>S: okay, let's keep talking about football. some people say that american football is too dangerouse and it should be abolished. what is your opinion on this comment?
 </p>
    Select one of the breakdown labels. (required)

    <div class="radio"><label><input name="17" required="true" type="radio" value="NOT BREAKDOWN" /><font color = "green">NOT A BREAKDOWN </label></div>

    <div class="radio"><label><input name="17" required="true" type="radio" value="POSSIBLE BREAKDOWN" /><font color = "#ffbf00">POSSIBLE BREAKDOWN </label></div>

    <div class="radio"><label><input name="17" required="true" type="radio" value="BREAKDOWN" /><font color = "red">BREAKDOWN </label></div>
    </div>
    </div>
    <br>


</div>
</div>
<!-- End Survey Layout --></section></crowd-form>
<!-- Please note that Bootstrap CSS/JS and JQuery are 3rd party libraries that may update their url/code at any time. Amazon Mechanical Turk (MTurk) is including these libraries as a default option for you, but is not responsible for any changes to the external libraries --><!-- External CSS references -->
<link crossorigin="anonymous" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" integrity="sha384-IS73LIqjtYesmURkDE9MXKbXqYA8rvKEp/ghicjem7Vc3mGRdQRptJSz60tvrB6+" rel="stylesheet" /><!-- Open internal style sheet -->
<style type="text/css">#collapseTrigger{
  color:#fff;
  display: block;
  text-decoration: none;
}
#submitButton{
  white-space: normal;
}
.image{
  margin-bottom: 15px; 
}
</style>
<!-- Close internal style sheet --><!-- External JS references --><script src="https://code.jquery.com/jquery-3.1.0.min.js" integrity="sha256-cCueBR6CsyA4/9szpPfrX3s49M9vUU5BgtiJj06wt/s=" crossorigin="anonymous"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js" integrity="sha384-s1ITto93iSMDxlp/79qhWHi+LsIi9Gx6yL+cOKDuymvihkfol83TYbLbOw+W/wv4" crossorigin="anonymous"></script><!-- Open internal javascript --><script>
  $(document).ready(function() {
    // Instructions expand/collapse
    var content = $('#instructionBody');
    var trigger = $('#collapseTrigger');
    // content.hide();
    $('.collapse-text').text('(Click to Collapse)');
    trigger.click(function(){
      content.toggle();
      var isVisible = content.is(':visible');
      if(isVisible){
        $('.collapse-text').text('(Click to Collapse)');
      }else{
        $('.collapse-text').text('(Click to Expand)');
      }
    });
    // end expand/collapse
  });
</script><!-- CLose internal javascript -->
<!-- YOUR HTML ENDS -->
]]>
</HTMLContent>
<FrameHeight>600</FrameHeight>
</HTMLQuestion>
    )"""