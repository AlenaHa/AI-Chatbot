export class Message{
    text: string;
    user: string;

    public constructor(_text: string, _user: string){
        this.text = _text;
        this.user = _user;
    }
}
