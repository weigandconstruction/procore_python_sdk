# AffectedBodyPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The display value for the affected body part | [optional] 
**value** | **str** | The value actually stored as affected body part. | [optional] 

## Example

```python
from procore_sdk.models.affected_body_part import AffectedBodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of AffectedBodyPart from a JSON string
affected_body_part_instance = AffectedBodyPart.from_json(json)
# print the JSON string representation of the object
print(AffectedBodyPart.to_json())

# convert the object into a dict
affected_body_part_dict = affected_body_part_instance.to_dict()
# create an instance of AffectedBodyPart from a dict
affected_body_part_from_dict = AffectedBodyPart.from_dict(affected_body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


