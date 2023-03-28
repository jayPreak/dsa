local Object1 = game.Workspace.Egg
local Object2 = game.Workspace.Banana
local Object3 = game.Workspace:FindFirstChild("Part1", true)
local Object4 = game.Workspace.Part
local Object5 = game.Workspace:FindFirstChild("Banana1", true)
local Object6 = game.Workspace:FindFirstChild("Egg1", true)
local Object7 = game.Workspace.Mouse
local Object8 = game.Workspace:FindFirstChild("Mouse1", true)
local Object9 = game.Workspace.Model:FindFirstChild("Part")
local Object10 = game.Workspace:FindFirstChild("Model1", true):FindFirstChild("Part", true)
--local Object11 = game.Workspace["iPhone (Contacts)"]:FindFirstChild("Decal", true)
--local Object12 = game.Workspace["iPhone (Contacts)1"]:FindFirstChild("Decal", true)
--local Ob





--print(type(Object1.Name))
--print(Object6.Name)
local starterGui = game:GetService("StarterGui")
local screenGui = starterGui:FindFirstChild("ScreenGui")
--local screenGui2 = starterGui:FindFirstChild("ScreenGui2")
--print(screenGui)
local textLabel = screenGui:FindFirstChild("Score")
--local textlabel2 = screenGui2:FindFirstChild("TextLabel")

--print(textLabel)


local lastObjectTouched = nil
local lastObjectTouchedtouched = false
local score = tonumber(-1)

function updateTextLabel(s)
	--textLabel.Text = "hello sexy"
	--print(textLabel.Text)
	local x = s
	textLabel.Text = "Score: " .. tostring(x)
	--print(textLabel.Text)
	--textLabel.
	--screenGui.Score. = "Score" .. s
end

local function updateGUI(s)
	print("Updating GUI with score:", s)
	updateTextLabel(s)
	--updateScore(score)
	-- update the GUI with the current score
end

local function onObjectTouched(object)
	if lastObjectTouched == nil then
		-- remember the last object touched by the player
		lastObjectTouched = object
		print("First object touched:", lastObjectTouched.Name)
		--lastObjectTouchedtouched = false
		--lastObjectTouched.touched = true
		--object:Destroy()
	else
		print("Second object touched:", object.Name)
		if object.Name == lastObjectTouched.Name .. "1" or object.Name .. "1" == lastObjectTouched.Name then
			-- destroy both objects and update the score
			
			lastObjectTouchedtouched = true
			--object.touched = true
			lastObjectTouched:Destroy()
			object:Destroy()
			score = score + 1
			print("Score updated:", score)
			--textlabel2.Text = "Yep: " .. score + 1
			--updateGUI(score)
			--updateTextLabel()
			lastObjectTouched = nil
		else
			lastObjectTouched = nil
		end
		-- reset the last object touched
		
	end
end

--for _, object in pairs(game.Workspace:GetChildren()) do
--	print("Object name:", object.Name)
--	--object.Touched:Connect(onObjectTouched)
--end
local function connectTouchedEvent(object)
	local hasExecuted = false -- flag to keep track of whether the function has executed for the current touch event
	object.Touched:Connect(function()
		if not hasExecuted then
			hasExecuted = true
			onObjectTouched(object)
			wait(1) -- wait for 1 second before resetting the flag, so that the function can be executed again for a new touch event
			hasExecuted = false
		end
	end)
end

--Object1.Touched:Connect(function() onObjectTouched(Object1) end)
--Object2.Touched:Connect(function() onObjectTouched(Object2) end)
--Object3.Touched:Connect(function() onObjectTouched(Object3) end)
--Object4.Touched:Connect(function() onObjectTouched(Object4) end)
--Object6.Touched:Connect(function() onObjectTouched(Object4) end)
--Object6.Touched:Connect(function() onObjectTouched(Object4) end)


connectTouchedEvent(Object1)
connectTouchedEvent(Object2)
connectTouchedEvent(Object3)
connectTouchedEvent(Object4)
connectTouchedEvent(Object5)
connectTouchedEvent(Object6)
connectTouchedEvent(Object7)
connectTouchedEvent(Object8)
connectTouchedEvent(Object9)
connectTouchedEvent(Object10)
connectTouchedEvent(Object11)
connectTouchedEvent(Object12)



