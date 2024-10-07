# CrewBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crew** | [**CostCode**](CostCode.md) |  | 

## Example

```python
from procore_sdk.models.crew_body import CrewBody

# TODO update the JSON string below
json = "{}"
# create an instance of CrewBody from a JSON string
crew_body_instance = CrewBody.from_json(json)
# print the JSON string representation of the object
print(CrewBody.to_json())

# convert the object into a dict
crew_body_dict = crew_body_instance.to_dict()
# create an instance of CrewBody from a dict
crew_body_from_dict = CrewBody.from_dict(crew_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


