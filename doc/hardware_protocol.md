# 通讯协议

## 协议格式

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度n</th> 
        <th bgcolor="#3FC65A">参数1</th> 
        <th bgcolor="#3FC65A">参数2</th> 
        <th bgcolor="#3FC65A">...</th> 
        <th bgcolor="#3FC65A">参数n</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>2</td>
        <td>2</td>
        <td>1</td>
        <td>1</td> 
        <td>1</td> 
        <td>1</td> 
        <td>1</td> 
        <td>1</td> 
        <td>1</td> 
        <td>1</td> 
        <td>1</td> 
        <td>2</td> 
    </tr> 
</table>

- 帧头：2字节固定为0x5B、0x7C
- 设备编码：2字节
- 帧类型：1字节 0x01（查询）、0x02（设置）、0x03（ACK）
- 校验位：从帧类型到数据结束的和 对256取余

## 公共协议

### 设备发送心跳

定时上报心跳，服务器无需响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x00</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

### 设置心跳间隔

推送配置心跳间隔消息请求

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">心跳间隔</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x00</td> 
        <td>0x02</td> 
        <td>0x01</td> 
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>
配置心跳间隔消息响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x00</td> 
        <td>0x02</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

### 更新设备编号

推送新的设备编号到设备

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">编号</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x00</td> 
        <td>0x03</td> 
        <td>0x02</td> 
        <td>0xXX 0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>
响应，并携带更细的设备编号

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">编号</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x00</td> 
        <td>0x03</td> 
        <td>0x02</td> 
        <td>0xXX 0xXX</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

## Demo设备

### 系统通讯协议

#### 设备登录

设备发送登录请求

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x01</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

设备登录成功响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x01</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

#### 系统推送配置消息

推送配置消息请求

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">环境上报间隔</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x01</td> 
        <td>0x02</td> 
        <td>0x01</td> 
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>
推送配置消息响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x01</td> 
        <td>0x02</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

### LED通讯协议

#### 发送设置LED颜色到设备

服务器推送LED颜色配置到设备

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">开关</th> 
        <th bgcolor="#3FC65A">R</th> 
        <th bgcolor="#3FC65A">G</th> 
        <th bgcolor="#3FC65A">B</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x02</td> 
        <td>0x01</td> 
        <td>0x04</td> 
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

设备发送响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x02</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

### 环境通讯协议

#### 设备上报环境数据

设备根据配置的环境上报间隔，定时上报环境温湿度数据

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">温度整数</th> 
        <th bgcolor="#3FC65A">温度小数</th> 
        <th bgcolor="#3FC65A">湿度整数</th> 
        <th bgcolor="#3FC65A">湿度小数</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x03</td> 
        <td>0x01</td> 
        <td>0x04</td> 
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

服务器发送接收到环境数据的响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x03</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

#### 服务器主动查询环境数据

服务器下发查询环境数据指令

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x01</td>
        <td>0x03</td> 
        <td>0x02</td> 
        <td>0x04</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>
设备响应服务器查询指令并携带环境数据

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">温度整数</th> 
        <th bgcolor="#3FC65A">温度小数</th> 
        <th bgcolor="#3FC65A">湿度整数</th> 
        <th bgcolor="#3FC65A">湿度小数</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x03</td> 
        <td>0x02</td> 
        <td>0x04</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>
### RTC时间推送到设备

服务器发送当前时间到设备

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">年</th> 
        <th bgcolor="#3FC65A">月</th> 
        <th bgcolor="#3FC65A">日</th> 
        <th bgcolor="#3FC65A">时</th> 
        <th bgcolor="#3FC65A">分</th> 
        <th bgcolor="#3FC65A">秒</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x04</td> 
        <td>0x01</td> 
        <td>0x06</td> 
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>
设备响应RTC消息

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x04</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

## Full103设备

### 系统通讯协议

#### 设备登录

设备发送登录请求

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x10</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

设备登录成功响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x10</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

#### 系统推送配置消息

推送配置消息请求

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">环境上报间隔</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x10</td> 
        <td>0x02</td> 
        <td>0x01</td> 
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

推送配置消息响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x10</td> 
        <td>0x02</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

### 环境通讯协议

#### 设备上报环境数据

设备根据配置的环境上报间隔，定时上报环境温湿度数据

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">温度整数</th> 
        <th bgcolor="#3FC65A">温度小数</th> 
        <th bgcolor="#3FC65A">湿度整数</th> 
        <th bgcolor="#3FC65A">湿度小数</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x11</td> 
        <td>0x01</td> 
        <td>0x04</td> 
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

服务器发送接收到环境数据的响应

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x11</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

#### 服务器主动查询环境数据

服务器下发查询环境数据指令

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x01</td>
        <td>0x11</td> 
        <td>0x02</td> 
        <td>0x04</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>


设备响应服务器查询指令并携带环境数据

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">温度整数</th> 
        <th bgcolor="#3FC65A">温度小数</th> 
        <th bgcolor="#3FC65A">湿度整数</th> 
        <th bgcolor="#3FC65A">湿度小数</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x11</td> 
        <td>0x02</td> 
        <td>0x04</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

### 继电器控制

#### 继电器开关设置

服务器发送继电器开关状态到设备，状态`0`:开，`1`:关

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#3FC65A">开关状态</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x02</td>
        <td>0x12</td> 
        <td>0x01</td> 
        <td>0x01</td> 
        <td>0xXX</td>
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>

设备响应RTC消息

<table>
    <tr>         
        <th bgcolor="#C68E3F">帧头</th>
        <th bgcolor="#BCC63F">设备编码</th>
        <th bgcolor="#3F8FC6">帧类型</th>
        <th bgcolor="#3F8FC6">指令类型</th> 
        <th bgcolor="#3F8FC6">指令编码</th> 
        <th bgcolor="#3FC6A3">参数长度</th> 
        <th bgcolor="#9B3FC6">校验位</th> 
        <th bgcolor="#C68E3F">帧尾</th> 
    </tr>     
    <tr>         
        <td>0x5B 0x7C</td>
        <td>0xXX 0xXX</td>
        <td>0x03</td>
        <td>0x12</td> 
        <td>0x01</td> 
        <td>0x00</td> 
        <td>0xXX</td> 
        <td>0x0D 0x0A</td> 
    </tr> 
</table>




# 服务器

websocket下发指令，发送到flask服务，发送对应的指令到消息队列，

硬件服务器接收到消息，发送数据，并记录发送状态到redis，

等待收到设备响应时更新redis中消息的状态

'指令编码_设备编码'：'状态 SEND:发送成功，等待设备响应 OK:响应成功 '

