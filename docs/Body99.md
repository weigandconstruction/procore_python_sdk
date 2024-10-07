# Body99


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**sub_job_id** | **int** | Unique identifier for the Sub Job | [optional] 
**standard_cost_code_list_id** | **int** | Unique identifier for the Standard Cost Code List | 

## Example

```python
from procore_sdk.models.body99 import Body99

# TODO update the JSON string below
json = "{}"
# create an instance of Body99 from a JSON string
body99_instance = Body99.from_json(json)
# print the JSON string representation of the object
print(Body99.to_json())

# convert the object into a dict
body99_dict = body99_instance.to_dict()
# create an instance of Body99 from a dict
body99_from_dict = Body99.from_dict(body99_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


