package libs
{
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class Characteristics extends Sprite
	{
		private var evalue:Number;
		private var dataValue:String;
		private var dataLoader:DataLoader;
		private var numTrans:ObjectValues;
		
		public function Characteristics( value:Number )
		{
		
			evalue = value;
			init();
		}
		
		private function init():void
		{
			dataLoader = new DataLoader("../data/characteristics.xml");
			dataLoader.addEventListener("ready",pullData);
				
		}
		
		public function get getCharDatavalue():String
		{
			return dataValue;
		}
		
		private function pullData(event:Event):void
		{
		var xmlStr:XML;
		xmlStr = event.target.getDatavalue;
		numTrans = new ObjectValues(String(evalue));
		dataValue = xmlStr[numTrans.getStr];
		
		dispatchEvent( new Event("ready"));
		
	
		}
	}
}