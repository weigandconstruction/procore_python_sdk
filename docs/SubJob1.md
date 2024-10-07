# SubJob1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sub Job ID | [optional] 
**name** | **str** | Sub Job Name | [optional] 
**code** | **str** | Sub Job Code | [optional] 

## Example

```python
from procore_sdk.models.sub_job1 import SubJob1

# TODO update the JSON string below
json = "{}"
# create an instance of SubJob1 from a JSON string
sub_job1_instance = SubJob1.from_json(json)
# print the JSON string representation of the object
print(SubJob1.to_json())

# convert the object into a dict
sub_job1_dict = sub_job1_instance.to_dict()
# create an instance of SubJob1 from a dict
sub_job1_from_dict = SubJob1.from_dict(sub_job1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


