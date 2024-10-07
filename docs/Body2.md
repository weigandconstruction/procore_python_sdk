# Body2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**status** | **str** | Subcontractor SOV status. Admin users or users with granular permissions to update the contract can chan ge the status if the contract has no requisitions (sub invoices) or approved commitment change orders. Bill recipients can change the status to &#39;under_review&#39; if the current status is &#39;draft&#39; or &#39;revise_and_resubmit.&#39; | 

## Example

```python
from procore_sdk.models.body2 import Body2

# TODO update the JSON string below
json = "{}"
# create an instance of Body2 from a JSON string
body2_instance = Body2.from_json(json)
# print the JSON string representation of the object
print(Body2.to_json())

# convert the object into a dict
body2_dict = body2_instance.to_dict()
# create an instance of Body2 from a dict
body2_from_dict = Body2.from_dict(body2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


