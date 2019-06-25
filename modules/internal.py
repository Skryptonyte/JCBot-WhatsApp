
import random
import builtins
wisequotes = ("`Bravery is not a function of firepower.`",
                  "`Human beings may not be perfect but a computer program with language synthesis is hardly an answer to the world's problem`",
                  "`Electronic surveillance doesn't inspire reverence. Maybe fear and obedience, but not reverence.`",
                  "`If there were no god, it would be necessary to invent him\n -- Voltaire`",
                  "`Better to reign in Hell, than serve in Heaven.\n -- Paradise Lost, John Milton`",
                  "`Yesterday, we obeyed kings and bent our necks before emperors.\nBut today, we kneel only to Truth...\n -- Kahlil Gibran`",
                  "`A forgotten virtue like honesty is worth at least twenty credits.`",
                  "`A system organized around the weakest qualities of individuals will produce these same qualities in its leaders.`"
                  )

print("Internal Module loaded..")

# General Commands

def jc_help():
    jcbot_sendMessage("This is a prototype bot that is currently not worth shit")

def jc_deusex():
    jcbot_sendMessage("My vision is augmented")

def jc_quotes():
    jcbot_sendMessage(wisequotes[random.randint(0,len(wisequotes)-1)])

def jc_test():
    jcbot_sendFile(argsList[1])

builtins.commands["help"] = jc_help
builtins.commands["deusex"] = jc_deusex
builtins.commands["wise"] = jc_quotes
builtins.commands["creep"] = jc_test
print(commands)
