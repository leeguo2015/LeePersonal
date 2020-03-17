$(document).ready(function () {
    var obj_username = $("#username");
    var obj_nickname = $("#nickname");
    var obj_password = $("#password");
    var obj_repassword = $("#repassword");
    var obj_email = $("#email");
    var obj_register = $("#sub_register");
    var send_true = true;

    obj_username.blur(function () {

        var result = CheckStr(obj_username.val());
        obj_username.css("border-style", "solid",);
        if (result === true) {

            obj_username.css("border-color", "green",);
            send_true = false;
        } else {
            obj_username.css("border-color", "red");
            send_true = true
        }
    });

    obj_nickname.blur(function () {

        var result = CheckStr(obj_nickname.val());
        obj_nickname.css("border-style", "solid",);
        if (result === true) {

            obj_nickname.css("border-color", "green",);
            send_true = false;

        } else {
            obj_nickname.css("border-color", "red");
            send_true = true
        }
    });

    obj_password.blur(function () {

        var result = CheckStr(obj_password.val());
        obj_password.css("border-style", "solid",);
        if (result === true) {

            obj_password.css("border-color", "green",);
            send_true = false;

        } else {
            obj_password.css("border-color", "red");
            send_true = true
        }
    });

    obj_repassword.blur(function () {
        var result = CheckStr(obj_repassword.val());
        obj_repassword.css("border-style", "solid",);
        if (result === true) {

            obj_repassword.css("border-color", "green",);
            send_true = false;

        } else {
            obj_repassword.css("border-color", "red");
            send_true = true
        }
    });

    obj_email.blur(function () {
        var result = CheckStr(obj_email.val());
        obj_email.css("border-style", "solid",);
        if (result === true) {

            obj_email.css("border-color", "green",);
            send_true = false;
        } else {
            obj_email.css("border-color", "red");
            send_true = true
        }
    });

    obj_register.click(
        //     $.ajax({
        //     url: "/user/register",              //请求地址
        //     type: "POST",                       //请求方式
        //     data: { name: "super", age: 20 },        //请求参数
        //     dataType: "json",
        //     success: function (response, xml) {
        //         // 此处放成功后执行的代码
        //     },
        //     fail: function (status) {
        //         // 此处放失败后执行的代码
        //     }
        // })


        $.post("/user/register/",
            {
                "user": {
                    'name': 'threedog',
                    'age': 18,
                    'sex': '男'
                },
                "password": "123456"
            },
            function (res) {
                console.log(res);
            })
    )


});


/**
 * @return {boolean}
 */
function CheckStr(Characters) {
    var SpecialCharacters = "[%--`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——| {}【】‘；：”“'。，、？]";
    for (let char of Characters) {
        if (SpecialCharacters.search(char) != -1) {
            return false;
        }
    }
    return true;
}