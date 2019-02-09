package libs
{
	public class ValueCalculator
	{
		import libs.NumberBreaker;
		import libs.ValueSpliter;
		import libs.CharValue;
		//--
		private var letter:CharValue;
		private var splitter:ValueSpliter;
		private var finalValue:NumberBreaker;
		private var textOutPut:String;
		//-- values generate form calculate function 
		private var vowelCount:Number = 0;
		private var consCount:Number = 0;
		private var letterCount:Number = 0;
		private var totalValue:Number = 0;
		//-- info section
		private var characteristics:Number = 0;
		private var soulUrge:Number = 0;
		private var outterExpression:Number = 0;
		private var initValue:String;
		private var intText:String;
		
		public function ValueCalculator( value:String )
		{
			initValue = value;
			init();
		}
		
		//--
		private function init():void
		{
			calculateValue( initValue );
		}
		
		// getters
		public function get getVowelCount():Number
		{
			return vowelCount;
		}
		
		//--
		public function get getConsCount():Number
		{
			return consCount;
		}
		
		public function get getTotalValue():Number
		{
			return totalValue;
		}
	
		//--
		public function get getLetterCount():Number
		{
			return letterCount;
		}
		
		//--
		public function get getCharacteristics():Number
		{
			finalValue = new NumberBreaker( totalValue );
			return Number( finalValue.getfinalResult );
		}
			//--
		public function get getRulingNumber():Number
		{
			finalValue = new NumberBreaker( totalValue );
			return Number( finalValue.getfinalResult );
		}
		//--
		public function get getBehaviour():Number
		{
			finalValue = new NumberBreaker( outterExpression );
			return finalValue.getfinalResult;
		}	//--
		public function get getOutterExpression():Number
		{
			finalValue = new NumberBreaker( outterExpression );
			return finalValue.getfinalResult;
		}
		//--
		public function get getSoulUrge():Number
		{
			finalValue = new NumberBreaker( soulUrge );
			return finalValue.getfinalResult;
		}
		
		//--
		public function get getInitValue():String
		{
			return initValue;
		}
		
		//--
		public function get getint():String
		{
			return intText;
		}
		
		//-----
		private function calculateValue( nameValue:String ):void
		{
		//-- value resseters
			 
			if ( nameValue.length > 0 )
			{
				splitter = new ValueSpliter( nameValue );
				CharValue.createSign( splitter.getNames, splitter.getObjYs );
				//-- loop throug letters
				for ( var i:Number = 0; i < splitter.getchars.length; i += 1 )
				{
					//-- set static charCount
					CharValue.charCount = splitter.getchars.length;
					CharValue.charArrLoc = ( i );
					letter = new CharValue( splitter.getchars[ i ]);
					if ( letter.isvowel )
					{
						vowelCount += 1;
						soulUrge += letter.hasintCharValue;
					}
					//-
					if ( !( letter.isvowel ))
					{
						consCount += 1;
						outterExpression += letter.hasintCharValue;
					}
					//-
					if ( letter.hasintCharValue > 0 )
					{
						letterCount += 1;
					}
					//-
					totalValue += letter.hasintCharValue;
					//trace(letter.hasmasterCharacterValue );
					// when loop end 
					if ( i == ( splitter.getchars.length - 1 ))
					{
						finalValue = new NumberBreaker( totalValue );
						textOutPut = "There are " + String( letterCount ) + " letters in your name.\nThose " + String( letterCount ) + " letters total to " + String( finalValue.getfinalResult ) + "\nThere are " + String( vowelCount ) + " vowels and " + String( consCount ) + " consonants in your name.";
						textOutPut += "\n<b>Characteristics Number</b> " + new NumberBreaker( this.totalValue ).getfinalResult + "\n<b>SoulUrge Number</b> " + new NumberBreaker( this.soulUrge ).getfinalResult + "\n<b>Outer Expression Number</b> " + new NumberBreaker( this.outterExpression ).getfinalResult;
						intText = textOutPut;
					}
						//-- 
				}
			}
		}
	}
}