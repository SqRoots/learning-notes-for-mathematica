# 收发邮件
> 客官别急，此文未完稿，作者正在玩命码字呢，先看看其它主题吧 ^_^

---

## 发送邮件

> 以 163 邮箱为例，其它邮箱类似

```mma
(*服务器信息*)
mailServer = "smtp.163.com";(*SMTP服务器*)
portNumber = 465;(*端口*)

(*收件人信息*)
to = "收件人邮箱地址";
cc = "抄送人邮箱地址";
bcc = "暗送人邮箱地址";

(*发件人信息*)
fromEmail = "yourName@163.com";(*发件人*)
user = "yourName";(*用户名*)
password = "xxxxxxxx";(*密码*)
encryptionProtocol = "SSL";(*加密方式*)

(*邮件内容*)s
ubject = "主题";
body = "正文";
attachments = "附件路径";

(*发送邮件*)
SendMail[
 "Server" -> mailServer,
 "PortNumber" -> portNumber,
 "To" -> to,
 "From" -> fromEmail,
 "UserName" -> user, "Password" -> password,
 "EncryptionProtocol" -> encryptionProtocol,
 "Subject" -> subject,
 "Body" -> body(*,
 "AttachedFiles"\[Rule]attachments*)]
```

## 接收邮件
