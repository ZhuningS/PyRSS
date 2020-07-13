const http = require("http");
const fs = require("fs");
const cheerio = require("cheerio");

http.get("http://tech.ifeng.com/", function(res) {
    // 设置编码
    res.setEncoding("utf8");
    // 当接收到数据时，会触发 "data" 事件的执行
    let html = "";
    res.on("data", function(data){
        html += data;
    });
    // 数据接收完毕，会触发 "end" 事件的执行
    res.on("end", function(){
        // 待保存到文件中的字符串
        let fileData = "";
        // 调用 cheerio.load() 方法，生成一个类似于 jQuery 的对象
        const $ = cheerio.load(html);
        // 接下来像使用 jQuery 一样来使用 cheerio
        $(".pictxt02").each(function(index, element) {
            const el = $(element);
            let link = el.find("h3 a").attr("href"),
                title = el.find("h3 a").text(),
                desc = el.children("p").text();

            fileData += `${link}\r\n${title}\r\n\t${desc}\r\n\r\n`;
        });

        // console.log("读取结束，内容：");
        // console.log(html);
        fs.writeFile("./source.txt", fileData, function(err) {
            if (err)
                return;
            console.log("成功")
        });
    })
});