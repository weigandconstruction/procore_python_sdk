# BodyPart


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
from procore_sdk.models.body_part import BodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPart from a JSON string
body_part_instance = BodyPart.from_json(json)
# print the JSON string representation of the object
print(BodyPart.to_json())

# convert the object into a dict
body_part_dict = body_part_instance.to_dict()
# create an instance of BodyPart from a dict
body_part_from_dict = BodyPart.from_dict(body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


