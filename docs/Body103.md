# Body103


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**standard_cost_code_list_id** | **int** | Standard Cost Code List ID | 
**standard_cost_code** | [**StandardCostCode2**](StandardCostCode2.md) |  | 

## Example

```python
from procore_sdk.models.body103 import Body103

# TODO update the JSON string below
json = "{}"
# create an instance of Body103 from a JSON string
body103_instance = Body103.from_json(json)
# print the JSON string representation of the object
print(Body103.to_json())

# convert the object into a dict
body103_dict = body103_instance.to_dict()
# create an instance of Body103 from a dict
body103_from_dict = Body103.from_dict(body103_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


