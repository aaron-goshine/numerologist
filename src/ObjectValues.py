package libs
{
	public class ObjectValues
	{
		private var mainObj:Object = new Object();
		private var resourseObj:Object = new Object();
		private var strValue:String;
		
		public function ObjectValues( numStr:String )
		{
			strValue = numStr;
			this.init();
		}
		
		private function init():void
		{
			this.mainObj = { "11": "eleven", "22": "twentytwo", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine" }
	
			this.resourseObj = { 
			"characteristics": { "url": "data/characteristics.xml", "type": "characteristics" },
			"rulingnumber": { "url": "data/rulingnumber.xml", "type": "rulingnumber" },
			"behaviour": { "url": "data/behaviour.xml", "type": "behaviour" },
			"outterexpression": { "url": "data/outterexpression.xml", "type": "outterexpression"},
			"soulurge": { "url": "data/soulurge.xml", "type": "soulurge" }
			
			}
				
		
		}
		
		
		public function get getStr():String
		{
			return this.mainObj[ strValue ];
		}
		
		public function get getTypeObj():Object
		{
			
			return this.resourseObj[ strValue ];
			
		}
	}
}