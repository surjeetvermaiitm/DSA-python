class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
    
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> suffix(n);
        vector<int> res(n);
        suffix[n-1]=1;
        int product=1;
        for(int i=n-2;i>=0;i--){
            suffix[i]=suffix[i+1]*nums[i+1];
        }
        for(int i=0;i<n;i++){
            res[i]=product*suffix[i];
            product=product*nums[i];
        }
        return res;
    }
};
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> suffix(n);
        suffix[n-1]=1;
        int prod_sofar=1;
        for(int i=n-2;i>=0;i--){
            prod_sofar=nums[i+1]*prod_sofar;
            suffix[i]=prod_sofar;
        }
        
        int p=1;
        for(int i=1;i<n;i++){
            p=p*nums[i-1];
            suffix[i]=suffix[i]*p;
        }
        return suffix;
    }
};