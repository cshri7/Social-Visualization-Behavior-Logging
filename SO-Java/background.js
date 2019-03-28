// chrome.runtime.onMessage.addListener(function(request, sender, callback) {
//   if (request.action == "xhttp") {
//
//     $.ajax({
//         type: request.method,
//         url: request.url,
//         data: request.data,
//         success: function(responseText){
//             callback(responseText);
//         },
//         error: function(XMLHttpRequest, textStatus, errorThrown) {
//             //if required, do some error handling
//             callback();
//         }
//     });
//
//     return true; // prevents the chrome.runtime.onMessage.addListener(function (msg,sender){callback from being called too early on return
//   }
// });

// console.log('Hi');
// alert('Hi');

chrome.runtime.onMessage.addListener(function (msg,sender){

  if((msg.from==='stackoverflowlog') && (msg.subject==='ask question'))
  {
    console.log('The user has asked a question');
    // console.log(msg.uid);
    var now = new Date().toLocaleString();
    var user_activity ={}
    user_activity['count']=1;
    user_activity['activity']='ask question';
    // user_activity['id']=msg.uid;
    user_activity['timestamp']=now;
    console.log(now);
    // alert('done');
  }

	if((msg.from==='stackoverflowlog') && (msg.subject==='vote-up'))
	{
		console.log('The user has up voted');
		// console.log(msg.uid);
    var now = new Date().toLocaleString();
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='vote-up';
		// user_activity['id']=msg.uid;
    user_activity['timestamp']=now;
    console.log(now);
    // alert('done');
	}

	if((msg.from==='stackoverflowlog') && (msg.subject==='vote-down'))
	{
		console.log('The user has down voted');
		// console.log(msg.uid);
    var now = new Date().toLocaleString();
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='vote-down';
		// user_activity['id']=msg.uid;
    user_activity['timestamp']=now;
    console.log(now);
    // alert('done');
	}

	if((msg.from==='stackoverflowlog') && (msg.subject==='favourite'))
	{
		console.log('The user has marked favourite');
		// console.log(msg.uid);
    var now = new Date().toLocaleString();
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='mark_favourite';
		// user_activity['id']=msg.uid;
    user_activity['timestamp']=now;
    console.log(now);
    // alert('done');
	}

	if((msg.from==='stackoverflowlog') && (msg.subject==='shared post'))
	{
		console.log('The user has shared a post');
		// console.log(msg.uid);
    var now = new Date().toLocaleString();
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='shared_posts';
		// user_activity['id']=msg.uid;
    user_activity['timestamp']=now;
    console.log(now);
    // alert('done');
	}

	if((msg.from==='stackoverflowlog') && (msg.subject==='commented on post'))
	{
		console.log('The user has entered a comment');
		// console.log(msg.uid);
    var now = new Date().toLocaleString();
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='comment';
		// user_activity['id']=msg.uid;
    user_activity['timestamp']=now;
    console.log(now);
    // alert('done');
	}

  $.post('http://127.0.0.1:5000/index',user_activity)

});
