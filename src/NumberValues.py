package libs
{
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class NumberValues extends Sprite
	{
		private var evalue:Number;
		private var typeValue:String;
		private var dataValue:String;
		private var dataLoader:DataLoader;
		private var numTrans:ObjectValues;
		
		public function NumberValues( value:Number,typeResource:String )
		{
		
			evalue = value;
			typeValue = typeResource;
			init();
		}
		
		private function init():void
		{		
			this.dataLoader = new DataLoader(typeValue);
			this.dataLoader.addEventListener("ready",pullData);
				
		}
		
		public function get getCharDatavalue():String
		{
			return this.dataValue;
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