class CharValue:
    charCount = 0
    charArrLoc = 0
    wordsigniture = []

    intChar = ''
    intCharValue = 0
    vowel = False
    masterCharacter = False
    masterCharacterValue = 0

    def __init__(self, chr):
        self.intChar = chr
        self.intCharValue = toNum(intChar)

    def hasintCharValue(self):
        return self.intCharValue


    def ismasterCharacter(self):
        return self.masterCharacter

    def hasmasterCharacterValue():
        return masterCharacterValue

    def toNum(self, letter):
        nmval = 0
        vowlSet = ('a', 'e', 'i', 'o', 'u', 'y')

        if (letter in vowlSet):
            self.vowel = True

        alpha = '#abcdefghijklmnopqrstuvwxyz'
        pos = alpha.index(letter)
        if pos % 11 == 0:
            return pos

        if pos % 9 == 0:
            return 9

        return pos % 9

    def createSign(self, wdArr, arrOfObjs):
        sigArr = []
        yObject = {}

        for ci in range(len(arrOfObjs)):

            charPosInfullStr = self.addArrIndexLimit(wdArr, arrOfObjs[ci])
            yObject = {}
            yObject.atCharIndex = charPosInfullStr
            yObject.atlocalIndex = arrOfObjs[ci].charPos
            yObject.inWord = arrOfObjs[ci].wordPos
            sigArr.push(yObject)

        def addArrIndexLimit(arrArr, limit):
            print ('yes')
            # finalCharPos = 0
            # for (var ai = 0; ai < (limit.wordPos); ai += 1):
            #     finalCharPos += (arrArr[ ai ].length)
            # // when loop ends
            # if (ai == (limit.wordPos)):
            #     finalCharPos += (limit.charPos)
            # return finalCharPos
            # wordsigniture = sigArr
