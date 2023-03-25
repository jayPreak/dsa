local Object1 = game.Workspace.Egg
local Object2 = game.Workspace.Banana
local Object3 = game.Workspace.Part
local Object4 = game.Workspace.Part

local lastObjectTouched = nil
local score = 0
local function updateGUI()
	print("Updating GUI with score:", score)
	-- update the GUI with the current score
end

local function onObjectTouched(object)
	if lastObjectTouched == nil then
		-- remember the last object touched by the player
		lastObjectTouched = object
		print("First object touched:", lastObjectTouched.Name)
	else
		print("Second object touched:", object.Name)
		if object.Name == lastObjectTouched.Name then
			-- destroy both objects and update the score
			lastObjectTouched:Destroy()
			object:Destroy()
			score = score + 1
			print("Score updated:", score)
			updateGUI()
		end
		-- reset the last object touched
		lastObjectTouched = nil
	end
end

for _, object in pairs(game.Workspace:GetChildren()) do
	print("Object name:", object.Name)
	--object.Touched:Connect(onObjectTouched)
end


Object1.Touched:Connect(function() onObjectTouched(Object1) end)
Object2.Touched:Connect(function() onObjectTouched(Object2) end)
Object3.Touched:Connect(function() onObjectTouched(Object3) end)
Object4.Touched:Connect(function() onObjectTouched(Object4) end)




-- anotherone

