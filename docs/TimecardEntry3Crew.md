# TimecardEntry3Crew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry3_crew import TimecardEntry3Crew

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry3Crew from a JSON string
timecard_entry3_crew_instance = TimecardEntry3Crew.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry3Crew.to_json())

# convert the object into a dict
timecard_entry3_crew_dict = timecard_entry3_crew_instance.to_dict()
# create an instance of TimecardEntry3Crew from a dict
timecard_entry3_crew_from_dict = TimecardEntry3Crew.from_dict(timecard_entry3_crew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


