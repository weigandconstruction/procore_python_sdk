# BodyPart1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Body Part ID | [optional] 
**name** | **str** | Body Part Name | [optional] 
**selectable** | **bool** | Represents whether a Body Part can be associated to an injury. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**parent_id** | **int** | Parent Body Part ID | [optional] 

## Example

```python
from procore_sdk.models.body_part1 import BodyPart1

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPart1 from a JSON string
body_part1_instance = BodyPart1.from_json(json)
# print the JSON string representation of the object
print(BodyPart1.to_json())

# convert the object into a dict
body_part1_dict = body_part1_instance.to_dict()
# create an instance of BodyPart1 from a dict
body_part1_from_dict = BodyPart1.from_dict(body_part1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


